# Permissions and Groups Setup

This Django application uses groups and permissions to manage user access:

## Custom Permissions:
- **can_view**: Allows users to view book details.
- **can_create**: Allows users to create new books.
- **can_edit**: Allows users to edit existing books.
- **can_delete**: Allows users to delete books.

## Groups and Assigned Permissions:
- **Editors**: can_create, can_edit
- **Viewers**: can_view
- **Admins**: can_view, can_create, can_edit, can_delete

## Views and Permissions:
- `book_detail`: Requires `can_view` permission.
- `book_create`: Requires `can_create` permission.
- `book_edit`: Requires `can_edit` permission.
- `book_delete`: Requires `can_delete` permission.