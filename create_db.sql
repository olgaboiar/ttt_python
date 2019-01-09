CREATE TABLE computer_best_moves (
            id SERIAL PRIMARY KEY,
            board_spots VARCHAR(9) NOT NULL,
            computer_marker VARCHAR(1) NOT NULL,
            best_move INT);
ALTER TABLE computer_best_moves ADD CONSTRAINT game_state UNIQUE (board_spots, computer_marker);