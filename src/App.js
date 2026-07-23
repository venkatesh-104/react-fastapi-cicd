import React, { useEffect, useState } from "react";

function App() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    fetch("http://54.66.29.95:8000")
      .then((res) => res.json())
      .then((data) => setEmployees(data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <h1>Employee Management System</h1>

      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Role</th>
          </tr>
        </thead>

        <tbody>
          {employees.map((emp) => (
            <tr key={emp.id}>
              <td>{emp.id}</td>
              <td>{emp.name}</td>
              <td>{emp.role}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;