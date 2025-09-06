// JavaScript Example: Reading Entities
// Filterable fields: teacher_id, full_name, subject, email, phone, address, qualification, experience_years, hire_date, status
async function fetchTeacherEntities() {
    const response = await fetch(`https://app.base44.com/api/apps/68bb29f90f1aa1b8808db4b6/entities/Teacher`, {
        headers: {
            'api_key': 'c7be281ac6e54739b50baa0475d5af93', // or use await User.me() to get the API key
            'Content-Type': 'application/json'
        }
    });
    const data = await response.json();
    console.log(data);
}

// JavaScript Example: Updating an Entity
// Filterable fields: teacher_id, full_name, subject, email, phone, address, qualification, experience_years, hire_date, status
async function updateTeacherEntity(entityId, updateData) {
    const response = await fetch(`https://app.base44.com/api/apps/68bb29f90f1aa1b8808db4b6/entities/Teacher/${entityId}`, {
        method: 'PUT',
        headers: {
            'api_key': 'c7be281ac6e54739b50baa0475d5af93', // or use await User.me() to get the API key
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updateData)
    });
    const data = await response.json();
    console.log(data);
}
