from __future__ import annotations

import json
import sqlite3
import time
from pathlib import Path
from typing import Any


class KernelStateStore:
    """Small SQLite state layer for modular kernel receipts and events."""

    def __init__(self, path: str | Path = "data/kernel_state.sqlite3") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init(self) -> None:
        with self._connect() as conn:
            conn.executescript(
                """
                create table if not exists kernel_events (
                    id integer primary key autoincrement,
                    created_at real not null,
                    event_type text not null,
                    module_id text,
                    token_sha256 text,
                    payload_json text not null
                );
                create index if not exists idx_kernel_events_type
                    on kernel_events(event_type);
                create index if not exists idx_kernel_events_module
                    on kernel_events(module_id);
                create index if not exists idx_kernel_events_token
                    on kernel_events(token_sha256);

                create table if not exists module_state (
                    module_id text primary key,
                    updated_at real not null,
                    state_json text not null
                );
                """
            )

    def record_event(
        self,
        event_type: str,
        payload: dict[str, Any],
        module_id: str | None = None,
        token_sha256: str | None = None,
    ) -> dict[str, Any]:
        created_at = time.time()
        with self._connect() as conn:
            cur = conn.execute(
                """
                insert into kernel_events
                    (created_at, event_type, module_id, token_sha256, payload_json)
                values (?, ?, ?, ?, ?)
                """,
                (
                    created_at,
                    event_type,
                    module_id,
                    token_sha256,
                    json.dumps(payload, sort_keys=True),
                ),
            )
        return {
            "id": cur.lastrowid,
            "created_at": created_at,
            "event_type": event_type,
            "module_id": module_id,
            "token_sha256": token_sha256,
        }

    def list_events(self, limit: int = 50) -> list[dict[str, Any]]:
        safe_limit = max(1, min(int(limit), 500))
        with self._connect() as conn:
            rows = conn.execute(
                """
                select id, created_at, event_type, module_id, token_sha256, payload_json
                from kernel_events
                order by id desc
                limit ?
                """,
                (safe_limit,),
            ).fetchall()
        return [self._row_to_event(row) for row in rows]

    def set_module_state(self, module_id: str, state: dict[str, Any]) -> dict[str, Any]:
        updated_at = time.time()
        with self._connect() as conn:
            conn.execute(
                """
                insert into module_state (module_id, updated_at, state_json)
                values (?, ?, ?)
                on conflict(module_id) do update set
                    updated_at = excluded.updated_at,
                    state_json = excluded.state_json
                """,
                (module_id, updated_at, json.dumps(state, sort_keys=True)),
            )
        return {"module_id": module_id, "updated_at": updated_at}

    def get_module_state(self, module_id: str) -> dict[str, Any] | None:
        with self._connect() as conn:
            row = conn.execute(
                "select module_id, updated_at, state_json from module_state where module_id = ?",
                (module_id,),
            ).fetchone()
        if row is None:
            return None
        return {
            "module_id": row["module_id"],
            "updated_at": row["updated_at"],
            "state": json.loads(row["state_json"]),
        }

    def _row_to_event(self, row: sqlite3.Row) -> dict[str, Any]:
        return {
            "id": row["id"],
            "created_at": row["created_at"],
            "event_type": row["event_type"],
            "module_id": row["module_id"],
            "token_sha256": row["token_sha256"],
            "payload": json.loads(row["payload_json"]),
        }
