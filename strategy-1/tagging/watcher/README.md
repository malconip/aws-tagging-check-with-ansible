# CloudFormation Template to Enforce AWS Tags
AWS provides Organization Tag Policies and Config Managed Rules to help you find improperly tagged resources, but neither of these tools prevents you from creating resources with missing or invalid tags. One way to proactively enforce your tagging strategy is by using the CloudFormation linter.

cfn-lint is a command-line tool that will make sure your AWS CloudFormation template is correctly formatted. It checks the formatting of your JSON or YAML file, proper typing of your inputs, and a few hundred other best practices. While the presence of specific tags isn’t checked by default, you can write a custom rule to do so in Python.

For example, if you want to ensure that your CloudFormation web servers follow the same rules as the Terraform example above and have:

1 -At least one AWS tag
2- The contact tag set to either j-mark or l-duke
3 -The env tag set
4 -The service tag set to cart or search

When you run cfn-lint, include your custom rule:


cfn-lint template.json -a ./path/to/custom/rules


If your CloudFormation template is missing any tags, you’ll see an error:


E9000 Missing Tag contact at Resources/WebServerInstance/Properties/Tags
template.json:169:9


Using linting to validate your AWS CloudFormation rules is a great way to enforce your AWS tags proactively. If you’re storing your CloudFormation templates in version control, you can run cfn-lint using pre-commit hooks or by making it part of your continuous integration workflow.

Because these rules are written in Python, they can be as complex as you need them to be, but they have drawbacks as well. linting rules won’t tell you about existing problems in resources that aren’t managed by CloudFormation, so they work best when combined with a reactive tag audit and adjustment strategy.
