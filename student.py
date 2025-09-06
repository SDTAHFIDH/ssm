// JavaScript Example: Reading Entities
// Filterable fields: student_id, full_name, class, grade_level, birth_date, gender, address, phone, parent_name, parent_phone, enrollment_date, status
async function fetchStudentEntities() {
    const response = await fetch(`https://app.base44.com/api/apps/68bb29f90f1aa1b8808db4b6/entities/Student`, {
        headers: {
            'api_key': 'c7be281ac6e54739b50baa0475d5af93', // or use await User.me() to get the API key
            'Content-Type': 'application/json'
        }
    });
    const data = await response.json();
    console.log(data);
}

// JavaScript Example: Updating an Entity
// Filterable fields: student_id, full_name, class, grade_level, birth_date, gender, address, phone, parent_name, parent_phone, enrollment_date, status
