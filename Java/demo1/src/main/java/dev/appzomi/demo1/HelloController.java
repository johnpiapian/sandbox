package dev.appzomi.demo1;

import dev.appzomi.api.User;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyEvent;

public class HelloController {
    @FXML
    private Label nameLabel;
    @FXML
    private TextField nameInput;
    @FXML
    private Label result;

    @FXML
    protected void onSubmitButtonClick(ActionEvent actionEvent) {
        searchUser();
    }

    @FXML
    protected void onNameInputEntered(KeyEvent event) {
        if (event.getCode().getCode() == 10) searchUser();
    }

    private void searchUser() {
        User u = User.getInstance();
        String searchResult = u.searchUser(nameInput.getText().toLowerCase());

        result.setText(searchResult == null ? "User not found!" : searchResult);
    }
}