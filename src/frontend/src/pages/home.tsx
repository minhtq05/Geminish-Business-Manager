// import EmailTable from "@/components/emailTable";
// import { analyticsTexts } from "@/data/constants";
// import Analytics from "@/components/analytics";
import graphics from "@/assets/nothinghere.jpg";
const Home: React.FC = () => {
  return (
    <div className="flex flex-col items-center justify-evenly gap-4">
      <p>Oops you have nothing here</p>
      <img src={graphics} alt="img" />
    </div>
  );
};

export default Home;
