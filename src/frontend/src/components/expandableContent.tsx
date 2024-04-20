import ShowMoreText from "react-show-more-text";
interface ExpandableComponentProps {
  content: React.ReactNode;
}
const ExpandableComponent: React.FC<ExpandableComponentProps> = ({
  content,
}: ExpandableComponentProps) => {
  return (
    <div>
      <ShowMoreText
        lines={3}
        more="Show more"
        less="Show less"
        anchorClass="text-blue-500"
        truncatedEndingComponent={"... "}
        expanded={false}
      >
        {content}
      </ShowMoreText>
    </div>
  );
};
export default ExpandableComponent;
