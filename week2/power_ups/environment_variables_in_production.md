### Environment Variables in Production 

**Restaurant equivalent**: This is like how different restaurant locations manage their information systems differently, but the end result is the same - your preferences are stored securely.

> **Note**: This section is optional reading for those interested in professional deployment environments.

In production environments, environment variables are typically set differently:

1. **Cloud Platforms:**
   - AWS: Parameter Store, Secrets Manager
   - Azure: App Configuration, Key Vault
   - Google Cloud: Secret Manager
   - Heroku: Config Vars

2. **Container Environments:**
   - Docker: Environment variables in Dockerfile or docker-compose.yml
   - Kubernetes: ConfigMaps and Secrets

3. **CI/CD Systems:**
   - GitHub Actions: Repository secrets
   - Jenkins: Credentials plugin
   - GitLab CI: CI/CD variables

### Best Practices for Environment Variables 

**Restaurant equivalent**: These are like the restaurant's policies for handling customer information:

1. **Never hardcode sensitive information** in your code or commit it to repositories (Don't write customer credit card numbers on napkins)
2. **Use different variables for different environments** (Different procedures for take-out vs. dine-in)
3. **Document required environment variables** in your project's README (Train staff on what customer information they need to collect)
4. **Add `.env` files to your `.gitignore`** to prevent accidental commits (Keep customer information in a locked drawer, not on public display)
5. **Use strong encryption** for sensitive values in production (Use a secure safe for storing customer payment details)
6. **Implement validation** to ensure required variables exist before running critical code (Verify you have all needed information before processing an order)

#### The .env.example Pattern 

One best practice we're using in this project is the `.env.example` pattern:

1. **Create a template file** (`.env.example`) with all required variables but dummy values
2. **Commit this template** to version control as documentation
3. **Never commit actual `.env` files** with real values
4. **Instruct new developers** to copy the example and add their own values:
   ```bash
   cp .env.example .env
   # Then edit .env with real values
   ```

This approach ensures that:
- New team members can easily see what environment variables are needed
- No sensitive information is exposed in version control
- Configuration requirements are well-documented
