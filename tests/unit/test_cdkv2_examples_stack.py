import aws_cdk as core
import aws_cdk.assertions as assertions

from cdkv2_examples.cdkv2_examples_stack import Cdkv2ExamplesStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdkv2_examples/cdkv2_examples_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Cdkv2ExamplesStack(app, "cdkv2-examples")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
