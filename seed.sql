CREATE DATABASE IF NOT EXISTS chatbotproject;
USE chatbotproject;


-- Create the chatbots table
CREATE TABLE chatbots (
    id INT AUTO_INCREMENT PRIMARY KEY,
    clerk_user_id VARCHAR(255) NOT NULL, -- Clerk's user ID
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Create the chatbot_characteristics table
CREATE TABLE chatbot_characteristics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chatbot_id INT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (chatbot_id) REFERENCES chatbots(id) ON DELETE CASCADE
);

-- Create the guests table
CREATE TABLE guests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Create the chat_sessions table
CREATE TABLE chat_sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chatbot_id INT NOT NULL,
    guest_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (chatbot_id) REFERENCES chatbots(id) ON DELETE CASCADE,
    FOREIGN KEY (guest_id) REFERENCES guests(id) ON DELETE SET NULL
);

-- Create the messages table
CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chat_session_id INT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    sender ENUM('user', 'ai') NOT NULL,
    FOREIGN KEY (chat_session_id) REFERENCES chat_sessions(id) ON DELETE CASCADE
);

-- Insert sample chatbot data
INSERT INTO chatbots (clerk_user_id, name) VALUES
('clerk_user_1', 'Customer Support Bot'),
('clerk_user_2', 'Sales Bot'),
('clerk_user_3', 'Tech Support Bot'),
('clerk_user_4', 'Feedback Bot'),
('clerk_user_5', 'Appointment Bot'),
('clerk_user_6', 'Billing Bot');

-- Insert sample chatbot characteristics data
INSERT INTO chatbot_characteristics (chatbot_id, content) VALUES
(1, 'You are a helpful customer support assistant.'),
(1, 'Our support hours are 9am-5pm, Monday to Friday.'),
(1, 'You can track your order on our website.'),
(2, 'You are a knowledgeable sales assistant.'),
(2, 'We offer a 30-day money-back guarantee on all products.'),
(2, 'Our products are available in various sizes and colors.'),
(3, 'You provide tech support for our software products.'),
(3, 'You can help troubleshoot installation issues.'),
(3, 'You can guide users through common troubleshooting steps.'),
(4, 'You collect feedback from customers after they make a purchase.'),
(4, 'You thank customers for their feedback and encourage them to be honest.'),
(4, 'You remind customers that their feedback helps improve products and services.'),
(5, 'You help customers schedule and manage appointments.'),
(5, 'You can reschedule appointments and send reminders.'),
(5, 'You confirm the details of each appointment with the customer.'),
(6, 'You assist with billing inquiries and payments.'),
(6, 'You can explain charges and help customers resolve billing issues.'),
(6, 'You provide invoices and payment receipts upon request.');

-- Insert sample guest data
INSERT INTO guests (name, email) VALUES
('Guest One', 'guest1@example.com'),
('Guest Two', 'guest2@example.com'),
('Guest Three', 'guest3@example.com'),
('Guest Four', 'guest4@example.com'),
('Guest Five', 'guest5@example.com'),
('Guest Six', 'guest6@example.com');

-- Insert sample chat session data
INSERT INTO chat_sessions (chatbot_id, guest_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(1, 3),
(4, 4),
(5, 5),
(6, 6);

-- Insert sample message data
INSERT INTO messages (chat_session_id, content, sender) VALUES
(1, 'Hello, I need help with my order.', 'user'),
(1, 'Sure, I can help with that. What seems to be the issue?', 'ai'),
(2, 'Can you tell me more about your products?', 'user'),
(2, 'Of course! We offer a variety of products. Which one are you interested in?', 'ai'),
(3, 'I am facing an installation issue.', 'user'),
(3, 'I can assist with that. Are you seeing any error messages?', 'ai'),
(4, 'What is your return policy?', 'user'),
(4, 'We offer a 30-day return policy on all items.', 'ai'),
(5, 'I would like to provide feedback on my recent purchase.', 'user'),
(5, 'We appreciate your feedback! Please share your thoughts.', 'ai'),
(6, 'I need to schedule an appointment.', 'user'),
(6, 'I can assist with scheduling your appointment. What date and time works for you?', 'ai'),
(7, 'I have a billing question.', 'user'),
(7, 'I can help with billing inquiries. What seems to be the issue?', 'ai');
