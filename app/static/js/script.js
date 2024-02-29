document
.getElementById("taskForm")
.addEventListener("submit", function (e) {
  e.preventDefault();
  const taskInput = document.getElementById("taskInput");
  const task = taskInput.value.trim();
  if (task) {
    // Implement the function to add tasks here
    addTask(task);
    taskInput.value = ""; // Clear input after adding
  }
});

function addTask(task) {
// Here you will make a POST request to your Flask backend to add a new task
// After adding the task, you can fetch and refresh the list of tasks
}

// Implement functions to fetch tasks, mark tasks as completed, and delete tasks

// Example function to fetch tasks
function fetchTasks() {
fetch("/tasks")
  .then((response) => response.json())
  .then((data) => {
    const taskList = document.getElementById("taskList");
    taskList.innerHTML = ""; // Clear existing tasks
    data.forEach((task) => {
      // For each task, create a DOM element and append it to the taskList
    });
  });
}

// Call fetchTasks on page load to populate the list
window.onload = function () {
fetchTasks();
};