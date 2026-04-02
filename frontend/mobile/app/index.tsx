import { View, Text, ScrollView, Pressable, StyleSheet } from "react-native";
import { useRouter } from "expo-router";

export default function Dashboard(){

  const router = useRouter();

  return(

    <ScrollView style={styles.container}>

      <Text style={styles.title}>
        Dashboard
      </Text>


      <View style={styles.card}>

        <Text style={styles.heading}>
          Sentinel Active
        </Text>

        <Text>
          High Rain Risk Detected
        </Text>

      </View>


      <View style={styles.card}>

        <Text style={styles.heading}>
          Trust Score
        </Text>

        <Text style={styles.big}>
          98%
        </Text>

      </View>


      <Pressable
        style={styles.card}
        onPress={()=>router.push("/pool")}
      >

        <Text style={styles.heading}>
          Community Pool
        </Text>

        <Text style={styles.big}>
          ₹1,50,000
        </Text>

        <Text>
          Tap to view details
        </Text>

      </Pressable>


      <View style={styles.card}>

        <Text style={styles.heading}>
          Weekly Premium
        </Text>

        <Text style={styles.big}>
          ₹30
        </Text>

      </View>

    </ScrollView>

  )

}



const styles = StyleSheet.create({

  container:{
    padding:20,
    backgroundColor:"#f1f5f9"
  },

  title:{
    fontSize:24,
    fontWeight:"bold"
  },

  card:{
    backgroundColor:"#ffffff",
    padding:18,
    borderRadius:12,
    marginTop:15
  },

  heading:{
    fontWeight:"bold",
    marginBottom:5
  },

  big:{
    fontSize:22,
    fontWeight:"bold"
  }

});