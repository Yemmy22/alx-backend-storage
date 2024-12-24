-- This Script Computes Average Weighted Score For User
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE w_avg_score FLOAT;
    
    SELECT SUM(c.score * p.weight) / SUM(p.weight)
    INTO w_avg_score
    FROM corrections AS c
    JOIN projects AS p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    UPDATE users 
    SET average_score = IFNULL(w_avg_score, 0)
    WHERE id = user_id;
END $$

DELIMITER ;
