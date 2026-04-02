import { View, Text, Pressable, StyleSheet } from "react-native";
import { useState } from "react";

type PlanProps = {
  title: string;
  price: string;
  desc: string;
};

export default function Policy(){

  const [plan,setPlan] = useState("");

  function PlanCard({ title, price, desc }: PlanProps){

    const selected = plan === title;

    return(

      <Pressable
        onPress={()=>setPlan(title)}
        style={[
          styles.card,
          selected && styles.selected
        ]}
      >

        <Text style={styles.heading}>
          {title}
        </Text>

        <Text>
          {price}
        </Text>

        <Text>
          {desc}
        </Text>

      </Pressable>

    )

  }


  return(

    <View style={styles.container}>

      <Text style={styles.title}>
        Policy Plans
      </Text>


      <PlanCard
        title="Basic"
        price="₹20/week"
        desc="Low Risk Coverage"
      />

      <PlanCard
        title="Moderate"
        price="₹30/week"
        desc="Medium Risk Coverage"
      />

      <PlanCard
        title="Premium"
        price="₹50/week"
        desc="High Risk + Peak Bonus"
      />


      {plan && (

        <View style={styles.result}>

          <Text>
            Selected Plan: {plan}
          </Text>

          <Text>
            Badge: Smart Insured Worker
          </Text>

        </View>

      )}

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
    marginTop:15,
    borderWidth:1,
    borderColor:"#e5e7eb"
  },

  selected:{
    borderColor:"#6366f1",
    borderWidth:2
  },

  heading:{
    fontWeight:"bold"
  },

  result:{
    marginTop:20,
    padding:18,
    backgroundColor:"#eef2ff",
    borderRadius:12
  }

});