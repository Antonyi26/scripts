import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

Window {
    visible: true
    width: 640
    height: 480
    //color: "tomato"

    ColumnLayout {
        anchors.fill: parent

        Item {
            height: 100
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter

            ListView {
                id: view
                anchors.fill: parent
                spacing: 2
                clip: true
                orientation: ListView.Horizontal
                model: myModel

                delegate: Rectangle {
                    height: 50
                    width: 100
                    color: model.color
                    radius: 10
                    border.color: "black"
                    border.width: 1

                    TextInput {
                        anchors.centerIn: parent
                        text: model.text
                        onAccepted: {
                            model.text = text
                        }
                    }
                }
            }
        }
    }
}
