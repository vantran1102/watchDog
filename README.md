<!DOCTYPE html>
<html>
<h1>File System and Directoriy Monitoring</h1>
<h2>Overview</h2>
<p>
This project is a File System and Directory Monitoring Application built using Python and the Watchdog library. The application monitors specified directories for file system events such as modifications, creations, and deletions. Whenever an event is detected, the application triggers predefined actions, such as backing up files, logging changes, or notifying users.
</p>
<h2>Key Features</h2>
<u>
    <li>Real-time monitoring of file system changes (file creation, modification, deletion).</li>
    <li>Automatic backup of files when changes are detected.</li>
    <li>Logs all events for auditing and tracking purposes.</li>
    <li>Recursive monitoring for directories and subdirectories.</li>
    <li>Highly customizable and extensible for different use cases (backup, file sync, etc.).</li>
</u>
<h2>Technologies Used</h2>
<ul>
    <li><strong>Python</strong>: A versatile programming language used to build the core of the application.</li>
    <li><strong>Watchdog</strong>: A Python library that allows the application to listen for file system events in real-time.</li>
</ul>
<h2>How It Works</h2>
<ol>
    <li>The user specifies a directory to monitor using a command-line argument.</li>
    <li>The application begins watching the directory and detects any file changes.</li>
    <li>Whenever a file is modified, created, or deleted, the application copies the file to a backup directory and logs the event.</li>
</ol>
</html>
