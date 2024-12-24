-- This Script Creates Index on First Letter of Name
CREATE INDEX idx_name_first ON names (name(1));
