from aws_cdk import (
    aws_apigateway as gateway,
    aws_lambda as lambda_,
    aws_certificatemanager as certificate,
    core
)


class MarkdownItSynapseLambdaStack(core.Stack):

  def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)


    DOMAIN_NAME = scope.node.try_get_context("DOMAIN_NAME")
    CERT_ARN = scope.node.try_get_context("CERT_ARN")

    fct = lambda_.Function(self, "mdlambda",
                           code=lambda_.AssetCode(path="./handler"),
                           handler="index.lambda_handler",
                           timeout=core.Duration.seconds(10),
                           runtime=lambda_.Runtime.NODEJS_8_10,
                           )

    api = gateway.RestApi(self,
                          "mdAPI",
                          domain_name=gateway.DomainNameOptions(
                              domain_name=DOMAIN_NAME,
                              certificate=certificate.Certificate.from_certificate_arn(self, "cert", CERT_ARN),
                              endpoint_type=gateway.EndpointType.REGIONAL)
                          )

    markdown2html = api.root.add_resource("markdown2html")
    markdown2html.add_method("POST", gateway.LambdaIntegration(fct))

