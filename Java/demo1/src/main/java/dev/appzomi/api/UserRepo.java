package dev.appzomi.api;

import java.util.ArrayList;
import java.util.Collection;

public class UserRepo {

    private Collection<String> names;

    public UserRepo() {
        names = new ArrayList<>() {
            {
                add("alice");
                add("bob");
                add("charlie");
                add("david");
                add("eve");
            }
        };
    }

    public Collection<String> getUserNames() {
        return this.names;
    }
}
