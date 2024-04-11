import EmailTable from "@/components/emailTable";
import { analyticsTexts } from "@/data/constants";
import Analytics from "@/components/analytics";
const Dashboard: React.FC = () => {
  return (
    <>
      <div className="flex flex-row items-center justify-betwwen gap-4 px-4">
        <EmailTable />
        <Analytics content={analyticsTexts} />
      </div>
    </>
  );
};

export default Dashboard;
