-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS autism_app;
USE autism_app;

-- Sample users
INSERT INTO `User` (user_id , name, age, gender, email)
VALUES
  (1, 'Alice Kim', 28, 'Female', 'alice@example.com'),
  (2, 'Ben Torres', 35, 'Male', 'ben@example.com');

-- Sample DNA Sequences and questionnaire responses
INSERT INTO DNA_Sequence (dna_id, user_id, sequence, evaluation, responses)
VALUES
  (1, 1, 'ATGCGTAGGCTAAGCCTAGG', 'Mild social indicators',
   JSON_OBJECT(
     'q1', 'yes',
     'q2', 'yes',
     'q3', 'no',
     'q4', 'no',
     'q5', 'yes',
     'q6', 'yes',
     'q7', 'no',
     'q8', 'no',
     'q9', 'yes',
     'q10', 'yes'
   )),

  (2, 2, 'CGTACGTAGCTAGCTAAGTC', 'No major indicators',
   JSON_OBJECT(
     'q1', 'no',
     'q2', 'no',
     'q3', 'no',
     'q4', 'no',
     'q5', 'no',
     'q6', 'no',
     'q7', 'no',
     'q8', 'no',
     'q9', 'no',
     'q10', 'no'
   ));
