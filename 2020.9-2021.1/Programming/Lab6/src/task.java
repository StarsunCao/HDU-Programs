import java.util.LinkedList;

public class task {
	private String title;
	private String description;
	private String deadline;
	private LinkedList<String> tags = new LinkedList<String>();
	
	task(String title){
		this.title = title;
	}
	
	public void setTitle(String inputTitle) {
		this.title = inputTitle;
	}
	public void setDescription(String iniputDescription) {
		this.description = iniputDescription;
	}
	public void setDeadline(String inputDeadline) {
		this.deadline = inputDeadline;
	}
	public void addTags(String inputTags) {
		this.tags.add(inputTags);
	}
	
	public String getTitle() {
		return title;
	}
	public String getDiscription() {
		return description;
	}
	public String getDeadline() {
		return deadline;
	}
	public LinkedList<String> getTags() {
		return tags;
	}
}
