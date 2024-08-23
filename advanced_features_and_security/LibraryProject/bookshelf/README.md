## Permissions and Groups Setup

### Custom Permissions:
- **can_view**: Allows viewing of the model.
- **can_create**: Allows creation of new model instances.
- **can_edit**: Allows editing of existing model instances.
- **can_delete**: Allows deletion of model instances.

### Groups:
- **Editors**: Assigned `can_edit` and `can_create` permissions.
- **Viewers**: Assigned `can_view` permission.
- **Admins**: Assigned all permissions (`can_edit`, `can_create`, `can_delete`, `can_view`).

### How to Use:
- Use the `@permission_required` decorator in views to restrict access based on these permissions.
