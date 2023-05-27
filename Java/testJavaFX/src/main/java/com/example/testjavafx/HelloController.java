package com.example.testjavafx;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;

public class HelloController {
    @FXML
    private Label welcomeText;
    @FXML
    private Button welcomeButton;

    @FXML
    protected void onHelloButtonClick() {
        welcomeText.setText("This is a text!");
    }

    @FXML
    protected void onHelloButtonHoverToggle() {
        String txt = "Hovered!";
        if(welcomeText.getText().equals(txt)) welcomeText.setText("");
        else welcomeText.setText(txt);
    }
}