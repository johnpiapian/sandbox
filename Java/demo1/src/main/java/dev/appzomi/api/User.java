package dev.appzomi.api;

public class User {
    public static User singleInstance = null;
    private final UserRepo userRepo;

    public User() {
        userRepo = new UserRepo();
    }

    public String searchUser(String name) {
        for (var user : userRepo.getUserNames()) {
            if (user.equals(name)) {
                return name;
            }
        }

        return null;
    }

    public static User getInstance() {
        if (singleInstance == null) singleInstance = new User();

        return singleInstance;
    }
}
