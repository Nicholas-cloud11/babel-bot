# Contributing Guidelines

Thank you for contributing to this project!

## Development Workflow

1. **Always work in a virtual environment**
   - Activate it before making any changes
   - This keeps dependencies isolated

2. **Pull before you start working**
   ```bash
   git pull origin main
   ```

3. **Create a branch for your work**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b bugfix/issue-description
   ```

4. **Make your changes**
   - Write clear, readable code
   - Add comments where necessary
   - Test your changes

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Clear description of what you changed"
   ```

6. **Push your branch**
   ```bash
   git push origin your-branch-name
   ```

7. **Create a Pull Request**
   - Go to GitHub
   - Click "New Pull Request"
   - Describe what your changes do
   - Request review from team members

## Best Practices

- **Commit messages**: Use clear, descriptive messages
  - Good: "Add user authentication function"
  - Bad: "update stuff"

- **Code style**: Keep it consistent with existing code

- **Dependencies**: If you add new packages, update `requirements.txt`
  ```bash
  pip freeze > requirements.txt
  ```

- **Don't commit**:
  - Virtual environment folders (venv/)
  - IDE configuration files
  - Sensitive information (passwords, API keys)
  - These are already in .gitignore

## Getting Help

If you're stuck:
1. Check existing documentation
2. Ask team members
3. Create an issue on GitHub
