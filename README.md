```markdown
# TechHorizon  
Event Management System  

This application was built using the **Django Web Framework**.  

## Getting Started  

Follow these steps to set up and run the application locally.  

### Prerequisites  
- Python: Install Python 3.13.0 or higher  
- Git: Ensure Git is installed on your machine  

### Installation Steps  

1. Clone the repository:  
   ```powershell/cmd
   git clone https://github.com/intelligencexi/techhorizon.git
   ```  

2. Navigate into the project directory:  
   ```powershell/cmd
   cd techhorizon
   ```  

3. Install Python 3.13.0 if not already installed.  

4. Install `virtualenv`:  
   ```powershell/cmd
   pip install virtualenv
   ```  

5. Create a virtual environment:  
   ```powershell/cmd
   virtualenv .techhorizon
   ```  

6. Activate the virtual environment:  
   ```powershell/cmd
   .techhorizon\Scripts\activate
   ```  

7. Install the dependencies:  
   ```powershell/cmd
   pip install -r requirements.txt
   ```  

### Running the Application  

1. Make migrations:  
   ```powershell/cmd
   py manage.py makemigrations
   ```  

2. Apply the migrations:  
   ```powershell/cmd
   py manage.py migrate
   ```  

3. Create an admin user:  
   ```powershell/cmd
   py manage.py createsuperuser
   ```  
   You can then access the admin panel at `http://localhost:8000/admin`.  

4. Start the development server:  
   ```powershell/cmd
   py manage.py runserver
   ```  

### Application Pages  

- **Homepage**: [http://localhost:8000](http://localhost:8000)  
- **Event Registration Page**: [http://localhost:8000/register/](http://localhost:8000/register/)  
- **Admin Registration Page** (no visible button for security reasons):  
  [http://localhost:8000/admin-register/](http://localhost:8000/admin-register/)  
- **Admin Login Page**: [http://localhost:8000/admin-login/](http://localhost:8000/admin-login/)  

### Notes  

- Only admin users can see the dashboard icon.  
- After logging out, the dashboard will no longer be accessible until you log back in as an admin.  

Feel free to contribute or report any issues with the application!
```  

You can copy this and save it as `README.md` in your repository. Make sure to test the instructions to confirm accuracy. 🚀
