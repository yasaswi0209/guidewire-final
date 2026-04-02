import { View, Text, StyleSheet } from "react-native";
import { theme } from "../theme/theme";

export default function Card({ title, children }) {

return (

<View style={styles.card}>

<Text style={styles.title}>
{title}
</Text>

{children}

</View>

);

}

const styles = StyleSheet.create({

card:{

backgroundColor: theme.card,

padding:18,

borderRadius:14,

borderWidth:1,

borderColor: theme.border,

marginBottom:15

},

title:{

fontSize:16,

fontWeight:"600",

color: theme.primary,

marginBottom:8

}

});