import { Tabs } from "expo-router";

export default function Layout(){

  return(

    <Tabs>

      <Tabs.Screen name="index" options={{title:"Dashboard"}} />

      <Tabs.Screen name="policy" options={{title:"Policy"}} />

      <Tabs.Screen name="claims" options={{title:"Claims"}} />

      <Tabs.Screen name="risk" options={{title:"Risk"}} />

    </Tabs>

  )

}