variable "project_id" {
  description = "Project ID where the Cloud SQL PostgreSQL instance will be created."
  type        = string
  default     = "your-project-id"
}

variable "region" {
  description = "Region where the Cloud SQL PostgreSQL instance will be created."
  type        = string
  default     = "your-region"
}

variable "db_instance_name" {
  description = "Name of the Cloud SQL PostgreSQL instance."
  type        = string
  default     = "your-instance-name"
}

variable "db_version" {
  description = "Version of the PostgreSQL database."
  type        = string
  default     = "POSTGRES_15"
}

variable "db_tier" {
  description = "Service tier of the Cloud SQL PostgreSQL instance."
  type        = string
  default     = "db-f1-micro"
}

variable "db_storage_size_gb" {
  description = "Storage size of the Cloud SQL PostgreSQL instance."
  type        = number
  default     = 100
}

variable "db_name" {
  description = "Name of the database to create within the Cloud SQL PostgreSQL instance."
  type        = string
  default     = "your-database-name"
}

variable "db_user" {
  description = "Name of the database user to create within the Cloud SQL PostgreSQL instance."
  type        = string
  default     = "your-database-user"
}

variable "db_password" {
  description = "Password of the database user to create within the Cloud SQL PostgreSQL instance."
  type        = string
  default     = "your-database-password"
}