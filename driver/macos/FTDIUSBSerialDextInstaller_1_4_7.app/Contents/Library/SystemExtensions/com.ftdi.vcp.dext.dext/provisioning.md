
Please include the line below in follow-up emails for this request.

Follow-up: 747748111

Hi Iain,

There two aspects to creating a provisioning profile that contains the necessary entitlements.

First, you need to create a new App ID that contains the DriverKit capability.  Note that the DriverKit capability is the very bottom of the capability step/page when creating a new App ID.

Next, you should create a new provisioning profile.  Associate the App ID (that you just created that has the DriverKit capability) with this provisioning profile.  When presented with the option to add additional entitlements to the provisioning profile you should select DriverKit from the entitlement pop-up menu.

After creating the provisioning profile you can do a very quick check that it contains the necessary/appropriate DriverKit entitlements by opening provisioning profile using a text editor.  

Althought most of a provisioning profile is raw binary (and will unintelligible in a text editor) the entitlements section should be plain text, and therefore be human readable. 

You should verify that the entitlements shown in the provisioning profle (notably the USB VID) exactly match the contents of the entitlements file in the Xcode project; the entitlements file in the Xcode project should not contain a USB PID if the entitlements section in the provisioning profile lacks a USB PID.  

If a dext built using the new provisioning profile still won't load when a matching device is connected then you should use the codesign tool to verify that the dext is properly signed and notarized.  Please do the following commands and send me their output (plain text, not screen capture):

codesign --verify --verbose /path/to/dext

codesign --test-requirement="=notarized" --verify --verbose /path/to/dext

Best regards,

Craigg



Hello, World!
