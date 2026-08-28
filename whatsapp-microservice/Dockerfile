FROM ghcr.io/puppeteer/puppeteer:latest

# Switch to root user to allow global installs or specific permission fixes if needed
USER root

# Create app directory
WORKDIR /app

# Copy package.json
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Ensure proper permissions for the node user
RUN chown -R pptruser:pptruser /app

# Switch back to the non-root user that comes with the puppeteer image
USER pptruser

# Expose the port
EXPOSE 3001

# Command to run the microservice
CMD ["npm", "start"]
