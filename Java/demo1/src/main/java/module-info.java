module dev.appzomi.demo1 {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.kordamp.bootstrapfx.core;

    opens dev.appzomi.demo1 to javafx.fxml;
    exports dev.appzomi.demo1;
}