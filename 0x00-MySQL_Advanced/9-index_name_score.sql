-- This Script Creates Composite Index on First Letter of Name and Score
CREATE INDEX idx_name_first_score ON names (name(1), score);
