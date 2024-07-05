Project: Educational Platform API

Description:
This Django project implements an educational platform API using Django REST Framework.
It provides endpoints for managing teachers, posts, and videos related to educational content.

Endpoints:
- /teachers/           (GET, POST)
- /teachers/<id>/      (GET, PUT, PATCH, DELETE)
- /teachers/<id>/posts/      (GET, POST)
- /teachers/<id>/posts/<id>/ (GET, PUT, PATCH, DELETE)
- /teachers/<id>/videos/     (GET, POST)
- /teachers/<id>/videos/<id>/ (GET, PUT, PATCH, DELETE)

Models:
- Teacher: Represents a teacher with fields like name, subject, bio.
- Post: Represents a post created by a teacher, includes fields like title, content, date_created.
- Video: Represents a video created by a teacher, includes fields like title, url, date_created.

Serializers:
- TeacherSerializer: Serializes/deserializes Teacher model data.
- PostSerializer: Serializes/deserializes Post model data.
- VideoSerializer: Serializes/deserializes Video model data.

Features:
- CRUD operations for teachers, posts, and videos.
- Nested endpoints for retrieving and managing posts and videos associated with specific teachers.
- Data validation using serializers.
- Authentication and permissions (to be implemented based on project requirements).
- Pagination and filtering (to be implemented based on project requirements).

Usage:
This API is designed to support educational content management, allowing users to create, read, update, and delete teachers, posts, and videos. It is structured to facilitate easy integration with frontend applications or other services requiring educational content management capabilities.
