output "public_ip" {
  value       = google_sql_database_instance.postgres.public_ip_address
  description = "The public IP address of your database"
}