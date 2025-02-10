
public class vector {
	private double x;
	private double y;
	private double z;
	
	public void setx(double inputx) {
		this.x = inputx;
	}	
	public void sety(double inputy) {
		this.y = inputy;
	}
	public void setz(double inputz) {
		this.z = inputz;
	}
	
	public double getx(){
		return x;
	}
	public double gety() {
		return y;
	}
	public double getz() {
		return z;
	}
	public double getlength() {
		double length = Math.sqrt(x*x + y*y + z*z);
		return length;
	}
	public String getstr() {
		return "[" + x + "," +  y + "," + z + "]";
	}
}
