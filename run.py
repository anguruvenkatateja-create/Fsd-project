from app import create_app

# 1. Initialize the app using the factory function
app = create_app()

# 2. This block is CRITICAL. It tells Python to run the server 
# ONLY if this specific file is executed directly.
if __name__ == "__main__":
    print("--- Starting the Hostel Management System ---")
    app.run(host='127.0.0.1', port=5000, debug=True)