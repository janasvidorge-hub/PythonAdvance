def report_formatter(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 50)
        result = func(*args, **kwargs)
        print("=" * 50)
        return result
    return wrapper


class DynamicReport:

    templates = {
        "Business": "Professional Format",
        "Education": "Academic Format",
        "Research": "Scientific Format"
    }

    def __init__(self, title, content, template):
        self.title = title
        self.content = content
        self.template = template.title().strip()

    @classmethod
    def add_template(cls, name, style):
        cls.templates[name.title().strip()] = style.strip()
        print(f"\nNew Template Added -> {name.title()}")

    def __str__(self):
        style = self.templates.get(self.template, "Default Format")
        return (
            f"Title      : {self.title}\n"
            f"Content    : {self.content}\n"
            f"Template   : {self.template}\n"
            f"Style      : {style}"
        )

    @report_formatter
    def display(self):
        print(self)


print("Available Templates:")
for t in DynamicReport.templates:
    print("-", t)

choice = input("\nDo you want to add a new template? (yes/no): ").strip().lower()

if choice == "yes":
    name = input("Template Name: ").strip()
    style = input("Template Style: ").strip()

    if name and style:
        DynamicReport.add_template(name, style)
    else:
        print("Template name and style cannot be empty.")

print("\nCreate Your Report")

title = input("Enter Report Title: ").strip()
content = input("Enter Report Content: ").strip()
template = input("Choose Template: ").strip()

report = DynamicReport(title, content, template)
report.display()