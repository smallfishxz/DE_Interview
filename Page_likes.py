CREATE TABLE IF NOT EXISTS coderpad.post_likes (ds VARCHAR(10), post_id INT, num_likes INT);
INSERT INTO coderpad.post_likes (ds, post_id, num_likes) VALUES ('2014-01-01', 101, 2);
INSERT INTO coderpad.post_likes (ds, post_id, num_likes) VALUES ('2014-01-01', 102, 7);
INSERT INTO coderpad.post_likes (ds, post_id, num_likes) VALUES ('2014-01-01', 103, 0);
INSERT INTO coderpad.post_likes (ds, post_id, num_likes) VALUES ('2014-01-01', 104, 9);
INSERT INTO coderpad.post_likes (ds, post_id, num_likes) VALUES ('2014-01-02', 102, 11);
INSERT INTO coderpad.post_likes (ds, post_id, num_likes) VALUES ('2014-01-02', 103, 2);
INSERT INTO coderpad.post_likes (ds, post_id, num_likes) VALUES ('2014-01-02', 104, 1);
INSERT INTO coderpad.post_likes (ds, post_id, num_likes) VALUES ('2014-01-02', 105, 7);

/*
Table contains the number of likes a post has received on a given datestamp (ds):

post_likes
+--------------+------------+------------+
| ds           | post_id    | num_likes  |
+--------------+------------+------------+
| 2014-01-01   | 101        | 2          |
| 2014-01-01   | 102        | 7          |
| 2014-01-01   | 103        | 0          |
| 2014-01-01   | 104        | 9          |
| 2014-01-02   | 102        | 11         |
| 2014-01-02   | 103        | 2          |
| 2014-01-02   | 104        | 1          |
| 2014-01-02   | 105        | 7          |
+--------------+------------+-------------
*/

/*
Write a query to return the dates that have > 20 likes.

Example Output:
+------------+ 
| ds         | 
+------------+ 
| 2014-01-02 | 
+------------+ 
*/

SELECT ds, SUM(num_likes) 
FROM post_likes
GROUP BY 1
HAVING SUM(num_likes) > 20

/* 
Write a single query to get the count of the following for a ds
* total number of posts
* total number of posts with > 0 likes

Example Output:
    +-------------+-----------+-----------------+
    | ds          | cnt_posts | cnt_posts_likes |
    +-------------+-----------+-----------------+
    | 2014-01-01  |     4     |       3         |
    | 2014-01-02  |     4     |       4         |
    +-------------+-----------+-----------------+
*/

SELECT ds, COUNT(distinct post_id) AS cnt_posts,
SUM(CASE WHEN num_likes > 0 THEN 1 ELSE 0 END) AS cnt_posts_likes
FROM post_likes
group by 1
