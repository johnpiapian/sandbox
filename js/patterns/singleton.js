class session {
  constructor() {
    this.loggedIn = true;
    this.userId = 1;
  }

  isLoggedIn() {
    return this.loggedIn;
  }

  setUserId(userId) {
    this.userId = userId;
  }

  getUserId() {
    return this.userId;
  }

  display() {
    console.log(`UserId: ${this.getUserId()}`)
  }
}

class singleSession {
  constructor() {
    this.session = null;
  }

  static getInstance() {
    if (this.session == null) this.session = new session();

    return this.session;
  }
}

a = singleSession.getInstance();
b = singleSession.getInstance();

a.display();
b.display();

a.setUserId(7);
a.display();
b.display();

b.setUserId(66);
a.display();
b.display();
