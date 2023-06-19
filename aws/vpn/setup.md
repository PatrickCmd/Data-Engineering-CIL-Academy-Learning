# Administrator Setup of a Client VPN Endpoint

## Notes for step 1

- For information about using EasyRSA in the AWS CLI to build and manage a PKI CA, see [EasyRSA 3 Quickstart Readme](https://github.com/OpenVPN/easy-rsa/blob/v3.0.6/README.quickstart.md).
To download the latest version of EasyRSA for Windows, go to https://github.com/OpenVPN/easy-rsa/releases. Unzip the folder, and run the EasyRSA-Start.bat file.
For more information about using the EasyRSA-Start.bat file, see [Client Authentication and Authorization](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/authentication-authorization.html).

## Additional resources

- For more information about setting up and using AWS Client VPN, see the [AWS Client VPN Administrator Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-getting-started.html).
- For more information about setting up authentication and authorization, see [Client Authentication and Authorization and Mutual Authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/authentication-authorization.html).
- For more information about using AWS certificates, see the [AWS Certificate Manager User Guide](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html).
- For more information about using split-tunnel, Split-Tunnel on AWS Client VPN Endpoints.
For more information using AWS Directory Service, see the [AWS Directory Service Administration Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html).

# Establishing a VPN Session with Client VPN

## Important notes

To connect remotely to the Client VPN endpoint, you need to install a VPN client. The following are two available options:

- [**AWS Client VPN for desktop (see the following screenshot)**](https://aws.amazon.com/vpn/client-vpn-download/)
- [**OpenVPN client**](https://openvpn.net/community-downloads/)

## Additional resources

- For more information about using Client VPN, see the [**AWS Client VPN User Guide**](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/user-getting-started.html).