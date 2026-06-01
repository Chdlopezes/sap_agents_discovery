"""Canonical project paths.

Every pipeline script imports from here so directories stay consistent.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INPUT_CSV = ROOT / "inputs" / "AI Features Data.csv"

PROMPT_ENRICH = ROOT / "prompt" / "prompt_enriquecimiento_ia_csv.md"
PROMPT_ANALYSIS = ROOT / "prompt" / "PROMPT_USO_IA_ESFUERZO.md"

ENRICHED_BATCHES_DIR = ROOT / "enriched_data" / "batches"
ENRICHED_FINAL = ROOT / "processed" / "AI_Features_Data_Enriched.xlsx"

EXEC_PROMPTS_DIR = ROOT / "executions" / "prompts"
EXEC_ANALYSES_DIR = ROOT / "executions" / "analyses"
EXEC_COMPILED_DIR = ROOT / "executions" / "compiled"
COMPILED_MD = EXEC_COMPILED_DIR / "analyses_compiled.md"

STATE_DIR = ROOT / "state"
ID_SLUG_MAP = STATE_DIR / "id_slug_map.json"
COMPILED_STATE = STATE_DIR / "compiled_state.json"

ENRICHED_SHEETS = ("AI Features & Agents", "Pricing Premium")
