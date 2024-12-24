-- This Script Computes Average Weighted Score For Users
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS u 
    SET u.average_score = (
        SELECT IFNULL(SUM(c.score * p.weight) / SUM(p.weight), 0)
        FROM corrections AS c
        JOIN projects AS p ON c.project_id = p.id
        WHERE c.user_id = u.id
    );
END $$

DELIMITER ;
