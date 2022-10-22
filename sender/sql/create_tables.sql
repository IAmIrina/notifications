-- Creation of product table
CREATE TABLE IF NOT EXISTS notifications (
  notification_id uuid NOT NULL,
  user_id uuid NOT NULL,
  content_id uuid NOT NULL,
  type varchar(250) NOT NULL);
