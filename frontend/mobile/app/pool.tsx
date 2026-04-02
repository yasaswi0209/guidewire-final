import { View, Text, StyleSheet } from "react-native";

export default function Pool(){

  return(

    <View style={styles.container}>

      <Text style={styles.title}>
        Community Pool
      </Text>


      <View style={styles.card}>

        <Text>Pool Amount</Text>

        <Text style={styles.big}>
          ₹1,50,000
        </Text>

        <Text>
          14250 workers protected
        </Text>

      </View>


      <View style={styles.card}>

        <Text>Nearby Workers</Text>

        <Text>Ravi – Swiggy</Text>

        <Text>Priya – Zomato</Text>

        <Text>Arjun – Swiggy</Text>

      </View>


      <View style={styles.card}>

        <Text>Recent Payouts</Text>

        <Text>Rain → ₹310</Text>

        <Text>Heat → ₹420</Text>

      </View>

    </View>

  )

}

const styles = StyleSheet.create({

  container:{
    padding:20
  },

  title:{
    fontSize:24,
    fontWeight:"bold"
  },

  card:{
    backgroundColor:"#fff",
    padding:18,
    borderRadius:12,
    marginTop:15
  },

  big:{
    fontSize:24,
    fontWeight:"bold"
  }

});