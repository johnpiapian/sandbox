// Base Handler Class
class Handler {
  setNext(handler) {
      this.nextHandler = handler;
      return handler;
  }

  handle(request) {
      if (this.nextHandler) {
          return this.nextHandler.handle(request);
      }
      return null; // exit case
  }
}

// Concrete Handlers
class UsernameExistsHandler extends Handler {
  handle(request) {
      if (!request.username) {
          return 'username is required';
      }
      return super.handle(request);
  }
}

class PasswordExistsHandler extends Handler {
  handle(request) {
      if (!request.password) {
          return 'password is required';
      }
      return super.handle(request);
  }
}

class UsernameLengthHandler extends Handler {
  handle(request) {
    if (request.username.length < 3) {
      return 'username must be at least 3 characters'
    }
    return super.handle(request)
  }
}

class PasswordLengthHandler extends Handler {
  handle(request) {
      if (request.password.length < 6) {
          return 'password must be at least 6 characters long';
      }
      return super.handle(request);
  }
}

// Client Code: Create a chain of handlers and process a request
const usernameHandler = new UsernameExistsHandler();
const passwordExistsHandler = new PasswordExistsHandler();
const usernameLengthHandler = new UsernameLengthHandler();
const passwordLengthHandler = new PasswordLengthHandler();

usernameHandler.setNext(passwordExistsHandler).setNext(usernameLengthHandler).setNext(passwordLengthHandler)

const request = {
  username: 'sut',
  password: 'pas3asd'
};

const validationErrored = usernameHandler.handle(request);

if (validationErrored) {
  console.log(`Validation failed: ${validationErrored}`);
} else {
  console.log('Validation succeeded, proceeding to login...');
}
