import { View, Text, ScrollView, StyleSheet } from "react-native";
import Card from "../components/Card";
import { theme } from "../theme/theme";

export default function Dashboard(){

return(

<ScrollView style={styles.container}>

<Text style={styles.heading}>
Worker Protection Dashboard
</Text>

<Card title="🛡 AI Sentinel">

<Text>
Heavy rain disruption detected
</Text>

</Card>


<Card title="🤖 Trust Score">

<Text style={styles.big}>
98%
</Text>

<Text>
✔ GPS verified
</Text>

<Text>
✔ Delivery pattern normal
</Text>

<Text>
✔ Peer match
</Text>

</Card>


<Card title="🌍 Community Pool">

<Text style={styles.big}>
₹1,50,000
</Text>

<Text>
14,250 workers protected
</Text>

</Card>

</ScrollView>

);

}

const styles = StyleSheet.create({

container:{
padding:18,
backgroundColor: theme.bg
},

heading:{
fontSize:22,
fontWeight:"700",
marginBottom:20,
color: theme.text
},

big:{
fontSize:28,
fontWeight:"700",
color: theme.primary
}

});