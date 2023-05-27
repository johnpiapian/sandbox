package test;

public class helloStatic {
	
	static hello x = new hello("test name");
	
	public static String greet() {
		return x.getName();
	}
}
