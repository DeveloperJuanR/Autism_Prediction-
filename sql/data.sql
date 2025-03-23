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


# -- Sample DNA Sequences and questionnaire responses
# INSERT INTO DNA_Sequence (dna_id, user_id, sequence, evaluation, responses)
# VALUES
#   (1, 1, 'ATGCGTAGGCTAAGCCTAGG', 'Mild social indicators',
#    JSON_OBJECT(
#      'Do you experience challenges with communication and social interactions?', 'yes',
#      'Do you find yourself having very focused or intense interests in specific subjects?', 'yes',
#      'Do you have a sibling who has been diagnosed with Autism Spectrum Disorder (ASD)?', 'no',
#      'Have you been diagnosed with a genetic or chromosomal condition, such as Fragile X syndrome?', 'no',
#      'Were your parents older when you were born?', 'yes',
#      'Do you often have trouble understanding if someone is joking or being sarcastic?', 'yes',
#      'Do bright lights or loud noises frequently cause you discomfort?', 'no',
#      'Did you have frequent temper tantrums or emotional outbursts as a child?', 'no',
#      'Do you frequently notice small details that others tend to overlook?', 'yes',
#      'Do you find small talk tiring or difficult?', 'yes'
#    )),
#
#   (2, 2, 'CGTACGTAGCTAGCTAAGTC', 'No major indicators',
#    JSON_OBJECT(
#     'Do you experience challenges with communication and social interactions?', 'no',
#      'Do you find yourself having very focused or intense interests in specific subjects?', 'no',
#      'Do you have a sibling who has been diagnosed with Autism Spectrum Disorder (ASD)?', 'no',
#      'Have you been diagnosed with a genetic or chromosomal condition, such as Fragile X syndrome?', 'no',
#      'Were your parents older when you were born?', 'no',
#      'Do you often have trouble understanding if someone is joking or being sarcastic?',  'no',
#      'Do bright lights or loud noises frequently cause you discomfort?', 'no',
#      'Did you have frequent temper tantrums or emotional outbursts as a child?', 'no',
#      'Do you frequently notice small details that others tend to overlook?',  'no',
#      'Do you find small talk tiring or difficult?',  'no'
#    ));